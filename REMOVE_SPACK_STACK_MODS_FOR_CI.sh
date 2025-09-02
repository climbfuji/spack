#!/usr/bin/env bash

set -e

if [ "$(uname)" == "Darwin" ]; then
  SED_PARAM="''"
else
  SED_PARAM=""
fi

sed -i ${SED_PARAM} 's/extensions:/#extensions:/g' ./etc/spack/defaults/config.yaml
sed -i ${SED_PARAM} 's/- ${SPACK_STACK_DIR}/#- ${SPACK_STACK_DIR}/g' ./etc/spack/defaults/config.yaml

sed -i ${SED_PARAM} 's/#builtin:/builtin:/g' ./etc/spack/defaults/repos.yaml
sed -i ${SED_PARAM} 's/#  git: https/  git: https/g' ./etc/spack/defaults/repos.yaml
sed -i ${SED_PARAM} 's/#  branch: /  branch: /g' ./etc/spack/defaults/repos.yaml
sed -i ${SED_PARAM} 's/builtin: ${SPACK_STACK_DIR}/#builtin: ${SPACK_STACK_DIR}/g' ./etc/spack/defaults/repos.yaml
sed -i ${SED_PARAM} 's/spack_stack: ${SPACK_STACK_DIR}/#spack_stack: ${SPACK_STACK_DIR}/g' ./etc/spack/defaults/repos.yaml

set +e

git diff || true
