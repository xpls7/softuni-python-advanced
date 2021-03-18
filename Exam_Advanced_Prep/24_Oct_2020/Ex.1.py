jobs = [int(el) for el in input().split(", ")]
job_index = int(input())


def min_cycles_for_job(job, job_index):
    sorted_jobs = sorted([(v, i) for (i, v) in enumerate(jobs)])
    cycles = 0
    for (job, index) in sorted_jobs:
        cycles += job
        if index == job_index:
            break
    return cycles


def print_result(result):
    print(result)


result = min_cycles_for_job(jobs, job_index)
print_result(result)
