import random
import time

def transmission(i, N,  totalNumberOfFrames):
    totalFramesSentandResent = 0
    while i <=  totalNumberOfFrames:
        z = 0
        for k in range(i, min(i + N,  totalNumberOfFrames + 1)):
            print(f"Sending Frame {k}...")
            totalFramesSentandResent += 1
        for k in range(i, min(i + N,  totalNumberOfFrames + 1)):
            f = random.randint(0, 1)
            if f == 1:
                print(f"Acknowledgment for Frame {k}...")
                z += 1
            else:
                print(f"Timeout!! Frame Number: {k} Not Received")
                print("Retransmitting Window...")
                break
        print()
        i += z
    return totalFramesSentandResent

def main():
    totalNumberOfFrames = int(input("Enter the Total number of frames: "))
    N = int(input("Enter the Window Size: "))
    i = 1
    start_time = time.time()
    totalFramesSentandResent = transmission(i, N, totalNumberOfFrames)
    end_time = time.time()
    print(f"Total number of frames which were sent and resent are: {totalFramesSentandResent}")
    print(f"Time taken: {end_time-start_time}")

if __name__ == "__main__":
    main()