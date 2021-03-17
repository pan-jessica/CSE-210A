load harness

@test "sub-1" {
    check '3 - 2' '1'
}

@test "sub-2" {
    check '5 - 3' '2'
}

@test "sub-3" {
    check '40 - 19' '21'
}

@test "sub-4" {
    check '-1 - 3' '-4'
}

@test "sub-5" {
    check '3 - -7' '10'
}

@test "sub-6" {
    check '-19 - -20' '1'
}

@test "sub-7" {
    check '30 - 16 - 5' '9'
}

@test "sub-8" {
    check '-1 - -2 - 3' '-2'
}

@test "sub-9" {
    check '100 - 25 - 50' '25'
}

@test "sub-10" {
    check '3 - 0 - 7' '-4'
}