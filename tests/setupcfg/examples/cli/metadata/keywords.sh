#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "$(mktemp -d)" || exit; { set +x; } 2>/dev/null; }

module="setupcfg.metadata.keywords"
set -- "keywords value"

( set -x; python -m "$module" "$@" )
value="$(set -x; python -m "$module")" || exit
echo $value
[[ "$value" == "$1" ]]
