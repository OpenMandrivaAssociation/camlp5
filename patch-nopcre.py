#!/usr/bin/env python3
"""Remove Pcre2 dependency from camlp5 sources."""
from pathlib import Path
import re

new_ocaml = '''let twodigit s = if String.length s = 1 then "0" ^ s else s;;
let normalize_version v =
  match String.split_on_char '_' v with
  | ["OCAML"; a; b] ->
      Printf.sprintf "OCAML_%s_%s_00" (twodigit a) (twodigit b)
  | ["OCAML"; a; b; c] ->
      Printf.sprintf "OCAML_%s_%s_%s" (twodigit a) (twodigit b) (twodigit c)
  | _ -> v
;;
'''

new_camlp5 = '''value twodigit s = if String.length s = 1 then "0"^s else s ;
value normalize_version v =
  match String.split_on_char '_' v with
  [ ["OCAML"; a; b] ->
      Printf.sprintf "OCAML_%s_%s_00" (twodigit a) (twodigit b)
  | ["OCAML"; a; b; c] ->
      Printf.sprintf "OCAML_%s_%s_%s" (twodigit a) (twodigit b) (twodigit c)
  | _ -> v ]
;
'''

for path, repl, pattern in [
    (
        Path('ocaml_src/meta/pa_macro.ml'),
        new_ocaml,
        r'let twodigit s = if String\.length s = 1 then "0" \^ s else s;;\s*'
        r'let normalize_version v =.*?;;',
    ),
    (
        Path('meta/pa_macro.ml'),
        new_camlp5,
        r'value twodigit s = if String\.length s = 1 then "0"\^s else s ;\s*'
        r'value normalize_version v =.*?;',
    ),
]:
    t = path.read_text()
    t2, n = re.subn(pattern, repl.strip(), t, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'failed to patch {path} (n={n})')
    path.write_text(t2)
    print('patched', path)
