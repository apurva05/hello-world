formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
                    "hello, what's up",
                    "how is it going",
                    "i am doing great in my office",
                    "everyone loves me")

