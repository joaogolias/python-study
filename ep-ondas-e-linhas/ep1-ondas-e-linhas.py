import math


def main():
    # ep1 = Ep1Ex1(4939950, 10, 25, 50)
    ep1 = Ep1Ex1(8992902, 10, 27, 75)
    print(ep1.params.attenuation)
    ep1.item_a()
    ep1.item_b()
    ep1.item_c()
    ep1.item_d()
    ep1.item_e()
    ep1.calculate_q_values(10)
    ep1.calculate_q_values(20)
    return


class Ep1Ex1Params:
    nusp = 0
    p = 0
    n = 0
    m = 0

    capacitance = 0
    propagation_speed = 0
    line_length = 0
    attenuation = 0

    generator_voltage = 0
    generator_resistance = 0
    line_resistance = 0

    def __init__(self, nusp, generator_voltage, generator_resistance, line_resistance):
        self.nusp = nusp
        self.generator_voltage = generator_voltage
        self.generator_resistance = generator_resistance
        self.line_resistance = line_resistance
        self.calculate_init_params()

    def calculate_init_params(self):
        self.p = self.nusp % 10
        self.n = (self.nusp//10) % 10
        self.m = (self.nusp//100) % 10
        self.calculate_attenuation()
        self.calculate_capacitance()
        self.calculate_speed()
        self.calculate_line_length()

    def calculate_attenuation(self):
        self.attenuation = (7 + self.m/10 + self.n/100 + self.p/1000)*1E-3
        # self.attenuation = (5 + self.m/10 + self.n/100 + self.p/1000)*1E-3

    def calculate_capacitance(self):
        self.capacitance = 1 + self.m/10 + self.n/100 + self.p/1000
        self.capacitance = self.capacitance*1E-9

    def calculate_speed(self):
        self.propagation_speed = (2 + self.m/10 + self.n/100 + self.p/1000)*1E8

    def calculate_line_length(self):
        self.line_length = (20 + self.m + self.n/10 + self.p/100)

    def print_init_params(self):
        print("m: ", self.m)
        print("n: ", self.n)
        print("p: ", self.p)
        print("capacitance: ", self.capacitance)
        print("propagation_speed: ", self.propagation_speed)
        print("line_length: ", self.line_length)


class Ep1Ex1:
    params = Ep1Ex1Params(0, 0, 0, 0)

    equivalent_resistance = 0
    generator_coefficient = 0
    initial_time = 0.2*1E-6

    new_inductance = 0
    new_capacitance = 0
    new_resistance = 0
    new_conductance = 0

    q_capacitance = 0
    q_inductance = 0

    def __init__(self, nusp, generator_voltage, generator_resistance, line_resistance):
        self.params = Ep1Ex1Params(nusp, generator_voltage, generator_resistance, line_resistance)
        self.calculate_coefficients()

    def calculate_coefficients(self):
        params = self.params
        self.equivalent_resistance = self.params.line_resistance/(self.params.line_resistance + self.params.generator_resistance)
        self.generator_coefficient = (params.generator_resistance - params.line_resistance)/(params.generator_resistance + params.line_resistance)

    def item_a(self):
        print("ITEM A: ")
        self.initial_time = 0.2*1E-6
        print("O v1 antes de 0.2us é: ", self.v_1_item_a(0))
        print("O v1 imediatamente depois de 0.2us é: ", self.v_1_item_a(0.2*1E-6))
        print()

    def item_b(self):
        print("ITEM B: ")
        print("O v1 para t infinto é: ", self.params.generator_voltage)
        print("O v2 para t infinto é: ", self.params.generator_voltage)
        print()

    def item_c(self):
        print("ITEM C: ")
        print("SIMULAR CIRCUITO")
        print()

    def item_d(self):
        print("ITEM D: ")
        print("A constante de tempo é: ", self.params.capacitance*self.params.line_resistance)
        print()

    def item_e(self):
        print("ITEM E: ")

        self.new_capacitance = 1/(self.params.propagation_speed*self.params.line_resistance)
        self.new_inductance = self.params.line_resistance/self.params.propagation_speed
        self.new_resistance = self.params.attenuation*self.params.line_resistance
        self.new_conductance = self.new_resistance*self.new_capacitance/self.new_inductance
        print("[F/m] C =  ", self.new_capacitance)
        print("[H/m] L =  ", self.new_inductance)
        print("[O/m] R =  ", self.new_resistance)
        print("[S/m] G =  ", self.new_conductance)

    def v_1_item_a(self, t):
        initial_time = 0.2*1E-6
        linear_coef = self.equivalent_resistance*self.params.generator_voltage

        b = (1+self.generator_coefficient)*linear_coef
        c = b*(1-2*math.exp(-(t-initial_time)/(self.params.line_resistance*self.params.capacitance)))

        heavy_side = 0
        if t >= initial_time:
            heavy_side = 1

        return linear_coef + c*heavy_side

    def calculate_q_values(self, n):
        print("EX2 - Item B para n = ", n)
        self.q_capacitance = self.new_capacitance*self.params.line_length/n
        self.q_inductance = self.new_inductance*self.params.line_length/n
        print("[F] Cq =  ", self.q_capacitance)
        print("[H] q_inductance =  ", self.q_inductance)
        print()


if __name__ == "__main__":
    main()
