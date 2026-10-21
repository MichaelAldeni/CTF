<?php
function is_hackerz($input) {
    foreach (['union', 'and'] as $keyword) {
        if (stripos($input, $keyword) !== false) {
            return true;
        }
    }
    return false;
}

$input = 'ununionion';
echo is_hackerz($input) ? 1 : 0;
echo $input;
