#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Function to generate primes using Sieve of Eratosthenes
int* sieve(int n, int* prime_count) {
    // Allocate boolean array for sieve
    char* is_prime = (char*)malloc((n + 1) * sizeof(char));
    memset(is_prime, 1, (n + 1) * sizeof(char));
    
    // 0 and 1 are not prime
    is_prime[0] = is_prime[1] = 0;
    
    // Sieve implementation
    for (int p = 2; p <= sqrt(n); p++) {
        if (is_prime[p]) {
            // Mark multiples as not prime
            for (int j = p * p; j <= n; j += p) {
                is_prime[j] = 0;
            }
        }
    }
    
    // Count and collect primes
    *prime_count = 0;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) {
            (*prime_count)++;
        }
    }
    
    // Allocate array for primes
    int* primes = (int*)malloc((*prime_count) * sizeof(int));
    int index = 0;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) {
            primes[index++] = i;
        }
    }
    
    free(is_prime);
    return primes;
}

// Modular exponentiation to handle large numbers
long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    
    while (exp > 0) {
        if (exp & 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp >>= 1;
    }
    
    return result;
}

// Find smallest number with 2^target_divisors divisors
long long find_number_with_divisors(int target_divisors) {
    // Generate initial prime list
    int prime_count;
    int* primes = sieve(8000000, &prime_count);
    
    // Initialize arrays for prime factor counts and weights
    int* prime_factor_counts = malloc(sizeof(int));
    long long* prime_factor_weights = malloc(sizeof(long long));
    
    prime_factor_counts[0] = 0;
    prime_factor_weights[0] = 0;
    int list_size = 1;
    
    // Constants for modular arithmetic
    const long long MOD = 500500507;
    
    // Iterate to find the number
    for (int iteration = 0; iteration < target_divisors; iteration++) {
        // Find minimum weight
        long long min_weight = prime_factor_weights[0];
        int min_index = 0;
        
        for (int i = 1; i < list_size; i++) {
            if (prime_factor_weights[i] < min_weight) {
                min_weight = prime_factor_weights[i];
                min_index = i;
            }
        }
        
        // Get next prime
        int next_prime = primes[list_size];
        prime_factor_counts[min_index]++;
        
        // Expand lists if needed
        if (min_index == list_size - 1) {
            list_size++;
            prime_factor_counts = realloc(prime_factor_counts, list_size * sizeof(int));
            prime_factor_weights = realloc(prime_factor_weights, list_size * sizeof(long long));
            
            prime_factor_counts[list_size - 1] = 1;
            prime_factor_weights[list_size - 1] = next_prime;
        } else {
            // Recalculate weight
            prime_factor_weights[min_index] = 
                mod_pow(primes[min_index], prime_factor_counts[min_index] + 1, MOD);
        }
    }
    
    // Calculate final result with modular multiplication
    long long result = 1;
    for (int i = 0; i < list_size; i++) {
        result = (result * mod_pow(primes[i], prime_factor_counts[i], MOD)) % MOD;
    }
    
    // Clean up
    free(primes);
    free(prime_factor_counts);
    free(prime_factor_weights);
    
    return result;
}

int main() {
    long long result = find_number_with_divisors(500501);
    
    printf("Smallest number with 2^500500 divisors: %lld\n", result);
    printf("Number of digits: %d\n", (int)log10(result) + 1);
    
    return 0;
}