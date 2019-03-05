#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "$(mktemp -d)" || exit; { set +x; } 2>/dev/null; }

module="setupcfg.options.scripts"
set -- "scripts/script1" "scripts/script2"

( set -x; python -m "$module" "$@" )
( set -x; cat setup.cfg )
value="$(set -x; python -m "$module")" || exit
echo $value
