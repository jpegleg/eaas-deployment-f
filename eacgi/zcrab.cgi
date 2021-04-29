#!/usr/bin/env bash
echo "Content-Type: text/html";
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
  echo "zcrabctf EXIT ERROR $?"
  exit 1
}
echo
echo "$(listener "$1" || errorout)"
echo
