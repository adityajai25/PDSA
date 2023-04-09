def no_overlap(L):
    L.sort(key=lambda x:x[2])
    applications_accepted = [L[0]]
    rem_applications = L[1:]
    for appl in rem_applications:
        last_accepted = applications_accepted[-1]
        if appl[1] > last_accepted[2]:
            applications_accepted.append(appl)
    customers_accepted = [a[0] for a in applications_accepted]
    return customers_accepted
