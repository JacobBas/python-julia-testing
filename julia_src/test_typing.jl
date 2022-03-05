# testing performance against type annotations
using BenchmarkTools

# without type annotation
a = []
for item in 1:1000
    push!(a, item)
end
print(a)

# with type annotation
a = Int[]
for item in 1:1000
    push!(a, item)
end
print(a)
