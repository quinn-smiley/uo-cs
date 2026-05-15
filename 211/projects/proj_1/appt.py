"""Appt and Agenda classes
Quinn Smiley, 2026-04-06, CS 211"""

from datetime import datetime

class Appt: 
    """An appointment has a start time, an end time, and a title.
    The start and end times should be on the same day.
    Usage example: 
        appt1 = Appt(datetime(2026, 3, 15, 13, 30), 
                     datetime(2026, 3, 15, 15, 30), "Nap")
        appt2 = Appt(datetime(2026, 3, 15, 15, 00), 
                     datetime(2026, 3, 15, 16, 00), "Coffee")
        if appt2 > appt1: 
            print(f"appt1, '{appt1}' was over when appt2 \ '{appt2}' started")
        elif appt1.overlaps(appt2):
            print("Oh no, a conflict in the schedule!")
            print(appt1.intersect(appt2))
    Should print:
        Oh no, a conflict in the schedule!
        2026-03-15 15:00 15:30 | Early afternoon nap and Coffee break
        """
    
    def __init__(self, start: datetime, finish: datetime, desc: str):
        assert finish > start
        f"Period finish ({finish}) must be after start ({start})"
        self.start = start
        self.finish = finish
        self.desc = desc
    
    def __str__(self) -> str:
        """The textual format of an appointment is
        yyyy-mm-dd hh:mm hh:mm | description
        Note that this is accurate only if the start and finish
        attributes occur on the same day.
        """
        date_iso = self.start.date().isoformat()
        start_iso = self.start.time().isoformat(timespec='minutes')
        finish_iso = self.finish.time().isoformat(timespec='minutes')
        return f"{date_iso} {start_iso} {finish_iso} | {self.desc}"
    
    def __repr__(self) -> str:
        return f"Appt({repr(self.start)}, {repr(self.finish)}, {repr(self.desc)})"

    def __eq__(self, other: 'Appt') -> bool:
        """Equality means same time period,
        ignoring description"""
        return self.start == other.start and self.finish == other.finish
    
    def __lt__(self, other) -> bool:
        """Less than means that an appointment is earlier than another"""
        return self.start < other.start and self.finish < other.finish
    
    def __gt__(self, other) -> bool: 
        """Greater than means that an appointment is later than another"""
        return self.start > other.start and self.finish > other.finish
    
    def overlaps(self, other) -> bool: # Used Cursor to condense my thinking
        """Is there a non-zero overlap between these periods?"""
        # answer = False
        # if (self.start).__gt__(other.start) and (self.start).__lt__(other.finish):
        #     answer = True
        # elif (other.start).__gt__(self.start) and (other.start).__lt__(self.finish):
        #     answer = True
        # return answer

        return self.start < other.finish and other.start < self.finish
    
    def intersect(self, other) -> bool:
        """The overlapping portion of the two Appt objects"""
        assert self.overlaps(other)
        lowest = min(self.finish, other.finish)
        highest = max(self.start, other.start)
        newApp = Appt(highest, lowest, "New Appointment")
        return newApp

    

    
if __name__ == "__main__":
    print("Running usage examples")

    # appt1 = Appt(datetime(2026, 3, 15, 13, 30),
    #             datetime(2026, 3, 15, 15, 30),
    #             "Early afternoon")

    appt1 = Appt(datetime(2026, 3, 15, 13, 30), datetime(2026, 3, 15, 15, 30), "Nap")
    appt2 = Appt(datetime(2026, 3, 15, 15, 00), datetime(2026, 3, 15, 16, 00), "Coffee")

    # eq test
    print(appt1 != appt2)

    # lt test
    print(appt1 < appt2)

    # gt test
    print(appt1 > appt2)

    # overlaps test
    print(appt1.overlaps(appt2))


    # intersect  & test
    print(str(appt1.intersect(appt2)))

    # repr test
    print(repr(appt1.intersect(appt2)))
    




class Agenda:
    """An Agenda is a collection of appointments,
    similar to a list.
    Usage:
    appt1 = Appt(datetime(2026, 3, 15, 13, 30),
    datetime(2026, 3, 15, 15, 30),
    "Early afternoon nap")
    appt2 = Appt(datetime(2026, 3, 15, 15, 00),
    datetime(2026, 3, 15, 16, 00),
    "Coffee break")
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
    print(f"Agenda has no conflicts")
    else:
    print(f"In agenda:\n{agenda.text()}")
    print(f"Conflicts:\n {ag_conflicts}")
    Expected output:
    In agenda:
    2026-03-15 13:30 15:30 | Early afternoon nap
    2026-03-15 15:00 16:00 | Coffee break
    Conflicts:
    2026-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """
    

    def __init__(self):
        self.elements = [ ]

    def __eq__(self, other: 'Agenda') -> bool:
        """Delegate to __eq__ (==) of wrapped lists"""
        return self.elements == other.elements
    
    def __len__(self) -> int: 
        return len(self.elements)
    
    def append(self, appt: "Appt"): # Used Cursor to understand what parameters to use
        return self.elements.append(appt)
    
    def __str__(self):
        """Each Appt on a separate line"""
        lines = [ str(e) for e in self.elements ]
        return "\n".join(lines)
    
    def __repr__(self) -> str:
        """The constructor does not work this way"""
        return f"Agenda({self.elements})"
    
    # Prep for sorting and finding conflicts
    def sort(self): 
        """Sort agenda by appointment start times"""
        self.elements.sort(key=lambda appt: appt.start)
    
    def conflicts(self) -> "Agenda": # Used Cursor to understand the problem and clean up my solution
        """Returns an agenda consisting of the conflicts
        (overlaps) between this agenda and the other.
        Side effect: This agenda is sorted
        """
        self.sort()
        appts = self.elements
        conflicts = Agenda()

        for i in range(len(appts)): 
            a = appts[i]
            for j in range(i + 1, len(appts)):
                b = appts[j]

                if b.start >= a.finish: 
                    break
                
                if a.overlaps(b):
                    conflicts.append(a.intersect(b))
        return conflicts



if __name__ == "__main__":
    print("Running usage examples")
    appt1 = Appt(datetime(2026, 3, 15, 13, 30),
    datetime(2026, 3, 15, 15, 30),
    "Early afternoon nap")
    appt2 = Appt(datetime(2026, 3, 15, 15, 00),
    datetime(2026, 3, 15, 16, 00),"Coffee break")
    if appt2 > appt1:
        print(f"appt1 '{appt1}' was over when appt2 '{appt2}' started")
    elif appt1.overlaps(appt2):
        print("Oh no, a conflict in the schedule!")
        print(appt1.intersect(appt2))
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda}")
        print(f"Conflicts:\n {ag_conflicts}")

