#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "$(mktemp -d)" || exit; { set +x; } 2>/dev/null; }

module="setupcfg.options.install_requires"
set -- "requires1" "requires2"

( set -x; python -m "$module" "$@" )
( set -x; cat setup.cfg )
value="$(set -x; python -m "$module")" || exit
echo $value
