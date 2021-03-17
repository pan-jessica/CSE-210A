load harness

@test "div-1" {
  check '9 / 3' '3'
}

@test "div-2" {
  check '-12 / 4' '-3'
}

@test "div-3" {
  check '0 / 2' '0'
}

@test "div-4" {
  check '100 / 5' '20'
}

@test "div-5" {
  check '50 / 2' '25'
}

@test "div-6" {
  check '-0 / -2' '0'
}

@test "div-7" {
  check '100 / 5 / 4' '5'
}

@test "div-8" {
  check '10 / -2 / 5' '-1'
}

@test "div-9" {
  check '1780218 / 9 / 99 / 999' '2'
}

@test "div-10" {
  check '1 / 1 / -1 / 1' '-1'
}