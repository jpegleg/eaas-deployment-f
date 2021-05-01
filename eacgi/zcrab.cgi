#!/usr/bin/env bash
echo "Content-Type: text/html";

[ -z "${GPXENV+x}" ] && export GPXENV="$2" || echo "ZCRAB >>> Found and set already, not using any new args for passphrase."

encryptor () {
  while read line; do
    echo "$(date +%Y%m%d%H%M%S)"
    echo "EaaS ZCRAB template"
    echo $line | sha256sum | cut -d' ' -f1
    echo $line | gpg --symmetric  --cipher=aes256 --always-trust --batch --armor --passphrase $GPXENV --yes --homedir=/root/
  done<&0
}

listener () {
  echo "$1" | encryptor | xxd -p | tr -d '\n'
}

errout () {
  echo "ZCRAB EaaS EXIT ERROR $?"
  exit 1
}
echo
echo "$(listener "$1" || errorout)"
echo
