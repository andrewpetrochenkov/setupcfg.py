#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "$(mktemp -d)" || exit; { set +x; } 2>/dev/null; }

module="setupcfg.metadata.version"
set -- "version value"

( set -x; python -m "$module" "$@" )
( set -x; cat setup.cfg ) || exit
value="$(set -x; python -m "$module")" || exit
echo $value
[[ "$value" == "$1" ]]
