#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "$(mktemp -d)" || exit; { set +x; } 2>/dev/null; }

module="setupcfg.options.py_modules"
set -- "py_module1" "py_module2"

( set -x; python -m "$module" "$@" )
( set -x; cat setup.cfg )
value="$(set -x; python -m "$module")" || exit
echo $value
