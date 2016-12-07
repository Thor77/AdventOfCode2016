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
	fmt.Printf("Password: %v\n", password)
}
