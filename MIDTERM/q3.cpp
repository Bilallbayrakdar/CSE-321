//  Quicksort sorts the elements of v in ascending order.
func Quicksort(v []int) {
    if len(v) < 20 {
        InsertionSort(v)
        return
    }
    p := Pivot(v)
    low, high := Partition(v, p)
    Quicksort(v[:low])
    Quicksort(v[high:])
}

func Pivot(v []int) int {
	n := len(v)
	return Median(v[rand.Intn(n)],
		v[rand.Intn(n)],
		v[rand.Intn(n)])
}

func Median(a, b, c int) int {
	if a < b {
		switch {
		case b < c:
			return b
		case a < c:
			return c
		default:
			return a
		}
	}
	switch {
	case a < c:
		return a
	case b < c:
		return c
	default:
		return b
	}
}


// Partition reorders the elements of v so that:
// - all elements in v[:low] are less than p,
// - all elements in v[low:high] are equal to p,
// - all elements in v[high:] are greater than p.
func Partition(v []int, p int) (low, high int) {
	low, high = 0, len(v)
	for mid := 0; mid < high; {
		// Invariant:
		//  - v[:low] < p
		//  - v[low:mid] = p
		//  - v[mid:high] are unknown
		//  - v[high:] > p
		//
		//         < p       = p        unknown       > p
		//     -----------------------------------------------
		// v: |          |          |a            |           |
		//     -----------------------------------------------
		//                ^          ^             ^
		//               low        mid           high
		switch a := v[mid]; {
		case a < p:
			v[mid] = v[low]
			v[low] = a
			low++
			mid++
		case a == p:
			mid++
		default: // a > p
			v[mid] = v[high-1]
			v[high-1] = a
			high--
		}
	}
	return
}


func InsertionSort(v []int) {
	for j := 1; j < len(v); j++ {
		// Invariant: v[:j] contains the same elements as
		// the original slice v[:j], but in sorted order.
		key := v[j]
		i := j - 1
		for i >= 0 && v[i] > key {
			v[i+1] = v[i]
			i--
		}
		v[i+1] = key
	}
}