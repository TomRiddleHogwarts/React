import random

def selective_repeat(N, tf):
    frames = [0] * (tf + 1)
    expected_frame = 1
    received_frames = []

    while expected_frame <= tf:
        unacknowledged_frames = []
        print("\nWindow:", expected_frame, "to", min(expected_frame + N - 1, tf))

        for k in range(expected_frame, min(expected_frame + N, tf + 1)):
            if frames[k] == 0:
                print(f"Sending Frame {k}...")
                f = random.randint(0, 1)
                if f == 0:
                    print(f"Timeout!! Frame {k} Not Received")
                    unacknowledged_frames.append(k)
                else:
                    print(f"Acknowledgment for Frame {k} received.")
                    frames[k] = 1
                    received_frames.append(k)

        while len(unacknowledged_frames) > 0:
            print("Retransmitting Frames:", unacknowledged_frames)
            for frame in unacknowledged_frames:
                if random.randint(0, 1):
                    print(f"Timeout!! Frame {frame} Not Received")
                else:
                    print(f"Acknowledgment for Frame {frame} received.")
                    received_frames.append(frame)
                    unacknowledged_frames.remove(frame)

        if len(received_frames) > 0:
            expected_frame = max(received_frames) + 1
        else:
            # If no acknowledgments received, repeat the same window
            expected_frame = expected_frame

    print("\nAcknowledgments received for all frames!")

def main():
    tf = int(input("Enter the Total number of frames: "))
    N = int(input("Enter the Window Size: "))
    selective_repeat(N, tf)

if __name__ == "__main__":
    main()
