###################################
# --- Day 8: Handheld Halting --- #
###################################

import AOCUtils

class VM:
    def __init__(self, program):
        self.program = program[:]

        self.pc = 0
        self.acc = 0

        self.seen = set()
        self.looped = False

    def run(self):
        while self.pc < len(self.program):
            if self.pc in self.seen:
                self.looped = True
                break

            self.seen.add(self.pc)

            inst, n = self.program[self.pc].split()
            n = int(n)

            if inst == "acc":
                self.acc += n
            elif inst == "jmp":
                self.pc += n-1
            elif inst == "nop":
                pass

            self.pc += 1

        if self.pc >= len(program):
            self.looped = False

###################################

program = AOCUtils.loadInput(8)

vm = VM(program)
vm.run()

print("Part 1: {}".format(vm.acc))

for i in range(len(program)):
    if "jmp" in program[i]:
        variation = program[:]
        variation[i] = program[i].replace("jmp", "nop")
    elif "nop" in program[i]:
        variation = program[:]
        variation[i] = program[i].replace("nop", "jmp")
    else:
        continue
    
    vm = VM(variation)
    vm.run()

    if not vm.looped:
        print("Part 2: {}".format(vm.acc))
        break

AOCUtils.printTimeTaken()