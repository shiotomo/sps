from batch import SpsBatch

class SpsSchedule:
    @staticmethod
    def main():
        sps_batch = SpsBatch()
        sps_batch.sps_service_schedule()

if __name__ == "__main__":
    SpsSchedule.main()