print("Welcome to The Referee – Decision Helper\n")

print("Choose a comparison:")
print("1. AWS EC2 vs AWS Lambda")
print("2. Python vs Java")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    print("\nAWS EC2 vs AWS Lambda\n")

    print("AWS EC2")
    print("Pros:")
    print("- Full control over the server")
    print("- Suitable for long running applications")
    print("Cons:")
    print("- Server management required")
    print("- Can be expensive if used continuously\n")

    print("AWS Lambda")
    print("Pros:")
    print("- No server management")
    print("- Cost effective for small tasks")
    print("Cons:")
    print("- Time limit on execution")
    print("- Less control over environment\n")

    print("Recommendation:")
    print("Use Lambda for short, event based tasks.")
    print("Use EC2 for applications that need full control.")

elif choice == "2":
    print("\nPython vs Java\n")

    print("Python")
    print("Pros:")
    print("- Easy to learn")
    print("- Short and readable code")
    print("Cons:")
    print("- Slower compared to Java\n")

    print("Java")
    print("Pros:")
    print("- Faster performance")
    print("- Widely used in large systems")
    print("Cons:")
    print("- More complex syntax\n")

    print("Recommendation:")
    print("Choose Python for beginners and rapid development.")
    print("Choose Java for large scale and performance critical systems.")

else:
    print("Invalid choice. Please run the program again.")