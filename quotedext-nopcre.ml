(* Hand-written unpack_qe (avoids ocaml-pcre2 build dependency).
   Matches: {(%|%%)<attrid>(<ws><delim>)?|<payload>|<attrs>} *)

exception Parse_error of string

let unpack_qe s =
  let n = String.length s in
  if n < 5 || s.[0] <> '{' || s.[n - 1] <> '}' then
    raise (Parse_error "quoted extension syntax");
  let i = ref 1 in
  let percents =
    if n > 2 && s.[1] = '%' && s.[2] = '%' then (i := 3; "%%")
    else if n > 1 && s.[1] = '%' then (i := 2; "%")
    else raise (Parse_error "expected % or %%")
  in
  let is_attrid_char c =
    c <> '%' && c <> '|' && c <> ' ' && c <> '\n' && c <> '\t' && c <> '}'
  in
  let start = !i in
  while !i < n - 1 && is_attrid_char s.[!i] do incr i done;
  if !i = start then raise (Parse_error "empty attrid");
  let attrid = String.sub s start (!i - start) in
  let ws_delim_opt =
    if !i < n - 1 && (s.[!i] = ' ' || s.[!i] = '\n' || s.[!i] = '\t') then begin
      let wstart = !i in
      while !i < n - 1 && (s.[!i] = ' ' || s.[!i] = '\n' || s.[!i] = '\t') do incr i done;
      let dstart = !i in
      while !i < n - 1 && s.[!i] <> '|' && s.[!i] <> ' ' && s.[!i] <> '\n'
            && s.[!i] <> '\t' && s.[!i] <> '}' do
        incr i
      done;
      Some (String.sub s wstart (!i - wstart))
    end else None
  in
  if !i >= n - 1 || s.[!i] <> '|' then raise (Parse_error "expected | after attrid");
  incr i;
  (* find last | before trailing attrs and closing } *)
  let payload_start = !i in
  let last_bar = String.rindex_from s (n - 2) '|' in
  if last_bar < payload_start then raise (Parse_error "missing payload separator");
  let payload = String.sub s payload_start (last_bar - payload_start) in
  (* group 4 in original was after second | - attrs; we don't return it *)
  (percents, attrid, ws_delim_opt, payload)

let make_string kind loc s =
  let (percents, attrid, ws_delim_opt, payload) = unpack_qe s in
  if percents <> kind then
    failwith (Printf.sprintf "Quotedext.make_string: kind %s was not found (saw <<%s>> instead)" kind percents) ;
  let payload_shift = 1 + (String.length percents) + (String.length attrid) +
                        (match ws_delim_opt with None -> 0 | Some s -> String.length s) +
                        1 in
  let payload_len = String.length payload in
  let payload_loc = Ploc.(sub loc payload_shift payload_len) in
  let attrid_loc = Ploc.(sub loc (1 + (String.length percents)) (String.length attrid)) in
  ((attrid_loc, attrid),(payload_loc,payload))
