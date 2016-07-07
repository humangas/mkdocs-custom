#!/bin/bash

TARGET_SHELL="main_build_gh-pages.sh"
cp -p ./$TARGET_SHELL $TMPDIR/$TARGET_SHELL
bash $TMPDIR/$TARGET_SHELL
