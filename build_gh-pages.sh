#!/bin/bash

TARGET_SHELL="build_gh-pages-main.sh"
cp -p ./$TARGET_SHELL $TMPDIR/$TARGET_SHELL
bash $TMPDIR/$TARGET_SHELL
