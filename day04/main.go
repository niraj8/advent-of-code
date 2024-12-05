package main

import (
	"io"
	"log"
	"os"
	"strings"
)

func main() {
	stdin, err := io.ReadAll(os.Stdin)
	if err != nil {
		log.Fatal("failed to read input", err)
	}
	input := strings.Split(string(stdin), "\n")

	grid := make([][]string, 0)
	for _, line := range input {
		grid = append(grid, strings.Split(line, ""))
	}
	log.Print(countXmas(grid))
	log.Print(countCrossMAS(grid))
}

func countXmas(grid [][]string) int {
	count := 0
	for x := range grid {
		for y := range grid {
			if grid[x][y] == "X" {
				count += check(grid, x, y)
			}
		}
	}
	return count
}

func countCrossMAS(grid [][]string) int {
	count := 0
	for x := range grid {
		for y := range grid {
			if x > 0 && x < len(grid[0])-1 && y > 0 && y < len(grid)-1 && grid[x][y] == "A" {
				if grid[x-1][y-1] == "M" && grid[x+1][y+1] == "S" && grid[x+1][y-1] == "M" && grid[x-1][y+1] == "S" {
					count += 1
				} else if grid[x-1][y-1] == "M" && grid[x+1][y+1] == "S" && grid[x-1][y+1] == "M" && grid[x+1][y-1] == "S" {
					count += 1
				} else if grid[x+1][y+1] == "M" && grid[x-1][y-1] == "S" && grid[x+1][y-1] == "M" && grid[x-1][y+1] == "S" {
					count += 1
				} else if grid[x+1][y+1] == "M" && grid[x-1][y-1] == "S" && grid[x-1][y+1] == "M" && grid[x+1][y-1] == "S" {
					count += 1
				}
			}
		}
	}
	return count
}

func check(grid [][]string, x, y int) int {
	return checkEast(grid, x, y) + checkWest(grid, x, y) + checkNorth(grid, x, y) + checkSouth(grid, x, y) + checkNW(grid, x, y) + checkNE(grid, x, y) + checkSE(grid, x, y) + checkSW(grid, x, y)
}

func checkEast(grid [][]string, x, y int) int {
	if x+3 < len(grid[0]) && grid[x+1][y] == "M" && grid[x+2][y] == "A" && grid[x+3][y] == "S" {
		return 1
	}
	return 0
}

func checkWest(grid [][]string, x, y int) int {
	if x-3 >= 0 && grid[x-1][y] == "M" && grid[x-2][y] == "A" && grid[x-3][y] == "S" {
		return 1
	}
	return 0
}

func checkNorth(grid [][]string, x, y int) int {
	if y-3 >= 0 && grid[x][y-1] == "M" && grid[x][y-2] == "A" && grid[x][y-3] == "S" {
		return 1
	}
	return 0
}

func checkSouth(grid [][]string, x, y int) int {
	if y+3 < len(grid) && grid[x][y+1] == "M" && grid[x][y+2] == "A" && grid[x][y+3] == "S" {
		return 1
	}
	return 0
}

func checkNW(grid [][]string, x, y int) int {
	if x-3 >= 0 && y-3 >= 0 && grid[x-1][y-1] == "M" && grid[x-2][y-2] == "A" && grid[x-3][y-3] == "S" {
		return 1
	}
	return 0
}

func checkSE(grid [][]string, x, y int) int {
	if x+3 < len(grid[0]) && y+3 < len(grid) && grid[x+1][y+1] == "M" && grid[x+2][y+2] == "A" && grid[x+3][y+3] == "S" {
		return 1
	}
	return 0
}

func checkNE(grid [][]string, x, y int) int {
	if x+3 < len(grid[0]) && y-3 >= 0 && grid[x+1][y-1] == "M" && grid[x+2][y-2] == "A" && grid[x+3][y-3] == "S" {
		return 1
	}
	return 0
}

func checkSW(grid [][]string, x, y int) int {
	if x-3 >= 0 && y+3 < len(grid) && grid[x-1][y+1] == "M" && grid[x-2][y+2] == "A" && grid[x-3][y+3] == "S" {
		return 1
	}
	return 0
}
