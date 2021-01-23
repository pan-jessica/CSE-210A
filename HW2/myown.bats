load harness

@test "myown-1" {
  check 'x := true ? 5 : 6' '{x → 5}'
}

@test "myown-2" {
  check 'temp := false ? 89 : 98' '{temp → 98}'
}

@test "myown-3" {
  check 'n := 3 < 9 ? 4 + 6 : 7 * 3' '{n → 10}'
}

@test "myown-4" {
  check 'n := 8 = -6 ? 4 * 6 : 8 / 2' '{n → 4}'
}

@test "myown-5" {
  check 'n := 3 > 1 ? 7 * 5 : 7 * 8' '{n → 35}'
}