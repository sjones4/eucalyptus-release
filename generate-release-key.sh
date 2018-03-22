#!/bin/bash
# Generate a GPG key for signing releases
#
# NOTE: If key generation hangs entropy generation may be required, e.g.
# install rng-tools and run: rngd -r /dev/urandom
set -euo pipefail

GPG_TEMP_HOME="$(pwd)/gpg-temp-home"
KEY_NAME="${1:-Eucalyptus Build}"
KEY_ADDR="${2:-build@appscale.com}"

if [ ! -z "${GPG_TEMP_HOME}" ] && [ -d "${GPG_TEMP_HOME}" ] ; then
  rm -rvf "${GPG_TEMP_HOME}"
fi
mkdir -v "${GPG_TEMP_HOME}"
cat > "${GPG_TEMP_HOME}"/gen-params <<EOF
     Key-Type: default
     Key-Length: 2048
     Subkey-Type: default
     Name-Real: ${KEY_NAME}
     Name-Email: ${KEY_ADDR}
     Expire-Date: 0
     %echo Generating key, see note in script if this takes too long...
     %commit
     %echo done
EOF
killall gpg-agent || true
gpg-agent --homedir "${GPG_TEMP_HOME}" --daemon \
  gpg2 \
    --homedir "${GPG_TEMP_HOME}" \
    --gen-key \
    --batch \
    "${GPG_TEMP_HOME}"/gen-params 2>/dev/null

cat > RPM-GPG-KEY-eucalyptus-release-as <<EOF
The following public key can be used to verify RPM packages built
and signed by AppScale Systems, Inc for Eucalyptus releases.

EOF
gpg2 --homedir "${GPG_TEMP_HOME}" --export --armour \
  2>/dev/null \
  | grep -v "^Version: " \
  >> RPM-GPG-KEY-eucalyptus-release-as

echo ""
echo ""
echo "Generated for \"${KEY_NAME} <${KEY_ADDR}>\""
echo ""
echo ""
echo "Public key output to RPM-GPG-KEY-eucalyptus-release-as, this"
echo "should be committed to the eucalyptus-release repository."
echo ""
echo ""
echo "Private key for use in Jenkins, Manage Jenkins / Configure System"
echo " / Global Passwords / GPG_KEY:"
echo "============ COPY BELOW THIS LINE ============"
gpg2 --homedir "${GPG_TEMP_HOME}" --export-secret-keys --armour \
  2>/dev/null \
  | grep -v 'PGP PRIVATE KEY BLOCK' \
  | grep -v Version \
  | xargs echo
echo "============ COPY ABOVE THIS LINE ============"
echo ""
if [ ! -z "${GPG_TEMP_HOME}" ] && [ -d "${GPG_TEMP_HOME}" ] ; then
  rm -rf "${GPG_TEMP_HOME}"
fi

