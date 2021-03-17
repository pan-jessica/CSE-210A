load harness

@test "mult-1" {
  check '9 * 3' '27'
}

@test "mult-2" {
  check '-3 * 4' '-12'
}

@test "mult-3" {
  check '0 * 2' '0'
}

@test "mult-4" {
  check '20 * 5' '100'
}

@test "mult-5" {
  check '0 * 2 * 5' '0'
}

@test "mult-6" {
  check '-2 * -0' '0'
}

@test "mult-7" {
  check '2 * 3 * 4 * 1000' '24000'
}

@test "mult-8" {
  check '1 * -2 * 3 * -4' '24'
}

@test "mult-9" {
  check '9 * 2 * 99 * 999' '1780218'
}

@test "mult-10" {
  check '1 * 1 * -1 * 1' '-1'
}
