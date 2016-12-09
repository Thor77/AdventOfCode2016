package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func is_full(s []string) bool {
	for _, a := range s {
		if a == "" {
			return false
		}
	}
	return true
}

func main() {
	file, err := os.Open("input/05")
	if err != nil {
		log.Fatal(err)
	}
	rawDoorID := make([]byte, 100)
	_, err = file.Read(rawDoorID)
	if err != nil {
		log.Fatal(err)
	}
	doorID := strings.Split(string(rawDoorID), "\n")[0]
	// PART 1
	password := ""
	for i := 0; len(password) < 8; i++ {
		// build string
		merged := doorID + strconv.Itoa(i)
		// md5
		hashed := md5.Sum([]byte(merged))
		// hex
		hexed := hex.EncodeToString(hashed[:])
		// check for leading zeros
		if strings.HasPrefix(hexed, "00000") {
			password += string(hexed[5])
		}
	}
	fmt.Printf("Password (Part1): %v\n", password)
	// PART 2
	password2 := make([]string, 8)
	for i := 0; !is_full(password2); i++ {
		// build string
		merged := doorID + strconv.Itoa(i)
		// md5
		hashed := md5.Sum([]byte(merged))
		// hex
		hexed := hex.EncodeToString(hashed[:])
		// check for leading zeros
		if strings.HasPrefix(hexed, "00000") {
			position, err := strconv.Atoi(string(hexed[5]))
			if err != nil {
				continue
			}
			if position < len(password2) && password2[position] == "" {
				password2[position] = string(hexed[6])
			}
		}
	}
	fmt.Printf("Password (Part2): %v\n", strings.Join(password2, ""))
}
