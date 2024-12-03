package main

import (
	"io"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func MustAtoi(str string) int {
	i, err := strconv.Atoi(str)
	if err != nil {
		log.Print(err)
		log.Fatalln("failed to convert string to int")
	}
	return i
}

func main() {
	stdin, err := io.ReadAll(os.Stdin)
	if err != nil {
		log.Fatal(err)
	}
	str := string(stdin)

	part1(str)
	part2(str)
}

func part1(input string) {
	var re = regexp.MustCompile(`(?m)mul\(\d{1,3},\d{1,3}\)`)

	result := 0
	for _, match := range re.FindAllString(input, -1) {
		result += parseMulMatch(match)
	}
	log.Print(result)
}

func parseMulMatch(match string) int {
	numbers := strings.Split(strings.TrimSuffix(strings.TrimPrefix(match, "mul("), ")"), ",")
	x := MustAtoi(numbers[0])
	y := MustAtoi(numbers[1])
	return x * y
}

func part2(input string) {
	var re = regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)`)
	result := 0
	toggle := true
	for _, match := range re.FindAllString(input, -1) {
		if match == "don't()" {
			toggle = false
			continue
		} else if match == "do()" {
			toggle = true
			continue
		}
		if toggle {
			result += parseMulMatch(match)
		}

	}
	log.Print(result)
}
