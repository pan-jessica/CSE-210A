
load harness

@test "myown-1" {
  check '2 - 3 * 4' '-10'
}

@test "myown-2" {
  check '6 + 9 - 3 * 2 + 7 - 4' '12'
}

@test "myown-3" {
  check '6 - 9 * 5 + 2' '-37'
}

@test "myown-4" {
  check '12 * 6 - 50' '22'
}

@test "myown-5" {
  check '-6 + -10 - 50 + 6 * 4' '-42'
}