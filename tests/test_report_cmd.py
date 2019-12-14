#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest
import os.path
import os

# ///////////////////////////////////////////////////////
#
# report sub-command tests
#
# ///////////////////////////////////////////////////////


def test_report_cmd_too_few_args(capsys):
    with pytest.raises(SystemExit):
        from fontline.app import main
        sys.argv = ['font-line', 'report']
        main()
        out, err = capsys.readouterr()
        assert err == "[font-line] ERROR: Missing file path argument(s) after the report subcommand."


def test_report_cmd_missing_file_request(capsys):
    from fontline.app import main
    sys.argv = ['font-line', 'report', 'missing.txt']
    main()
    out, err = capsys.readouterr()
    assert err.startswith("[font-line] ERROR: ")


def test_report_cmd_unsupported_filetype(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'bogus.txt')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert err.startswith("[font-line] ERROR: ")


def test_report_cmd_reportstring_filename(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "Hack-Regular.ttf " in out


def test_report_cmd_reportstring_version(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "Version 2.020;DEV-03192016;" in out


def test_report_cmd_reportstring_sha1(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "SHA1: 638f033cc1b6a21597359278bee62cf7e96557ff" in out


def test_report_cmd_reportstring_upm(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[head] Units per Em:   2048" in out


def test_report_cmd_reportstring_ymax(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[head] yMax:           2001" in out


def test_report_cmd_reportstring_ymin(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[head] yMin:          -573" in out


def test_report_cmd_reportstring_capheight(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] CapHeight:      1493" in out


def test_report_cmd_reportstring_xheight(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] xHeight:        1120" in out


def test_report_cmd_reportstring_typoascender(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] TypoAscender:   1556" in out


def test_report_cmd_reportstring_typodescender(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] TypoDescender: -492" in out


def test_report_cmd_reportstring_winascent(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] WinAscent:      1901" in out


def test_report_cmd_reportstring_windescent(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] WinDescent:     483" in out


def test_report_cmd_reportstring_ascent(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] Ascent:         1901" in out


def test_report_cmd_reportstring_descent(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] Descent:       -483" in out


def test_report_cmd_reportstring_linegap(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] LineGap:        0" in out


def test_report_cmd_reportstring_typolinegap(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] TypoLineGap:    410" in out


def test_report_cmd_reportstring_typoA_typodesc(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] TypoAscender to TypoDescender:  2048" in out


def test_report_cmd_reportstring_winA_windesc(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] WinAscent to WinDescent:        2384" in out


def test_report_cmd_reportstring_ascent_descent(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] Ascent to Descent:              2384" in out


def test_report_cmd_reportstring_winA_typoasc(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] Ascent to [OS/2] TypoAscender:       345" in out


def test_report_cmd_reportstring_ascent_typoasc(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] Ascent to [OS/2] TypoAscender:       345" in out


def test_report_cmd_reportstring_winD_typodesc(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] WinDescent to [OS/2] TypoDescender:  -9" in out


def test_report_cmd_reportstring_descent_typodesc(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[hhea] Descent to [OS/2] TypoDescender:     -9" in out


def test_report_cmd_reportstring_typo_to_upm(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "typo metrics / UPM:  1.2" in out


def test_report_cmd_reportstring_win_to_upm(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "win metrics  / UPM:  1.16" in out


def test_report_cmd_reportstring_hhea_to_upm(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "hhea metrics / UPM:  1.16" in out


def test_report_cmd_reportstring_fsselection_bit7_set_true(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular-fsSelection-bit7-set.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] fsSelection USE_TYPO_METRICS bit set: True" in out


def test_report_cmd_reportstring_fsselection_bit7_set_false(capsys):
    from fontline.app import main
    filepath = os.path.join('tests', 'testingfiles', 'Hack-Regular.ttf')
    sys.argv = ['font-line', 'report', filepath]
    main()
    out, err = capsys.readouterr()
    assert "[OS/2] fsSelection USE_TYPO_METRICS bit set: False" in out


# TODO: add tests for new baseline to baseline distance calculations in report
