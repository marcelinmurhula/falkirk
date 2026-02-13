from manim import *


class FalkirkWheelLowPoly(ThreeDScene):
    def construct(self):

        # ---------------------------
        # Camera
        # ---------------------------
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        # ---------------------------
        # Step Title
        # ---------------------------
        step_text = Text("1. Boats Enter Caissons").scale(0.6)
        step_text.to_edge(UP)
        self.add_fixed_in_frame_mobjects(step_text)
        self.play(FadeIn(step_text))

        # ---------------------------
        # Axle (center)
        # ---------------------------
        axle = Cylinder(radius=0.2, height=4, direction=UP)
        axle.set_fill(GRAY, opacity=1)

        # ---------------------------
        # Caissons (use Prism instead of Box)
        # ---------------------------
        caisson_top = Prism(dimensions=[3, 1, 0.6])
        caisson_bottom = Prism(dimensions=[3, 1, 0.6])

        caisson_top.set_fill(BLUE_E, opacity=1)
        caisson_bottom.set_fill(BLUE_E, opacity=1)

        caisson_top.shift(UP * 2)
        caisson_bottom.shift(DOWN * 2)

        wheel_group = VGroup(caisson_top, caisson_bottom)

        # ---------------------------
        # Boats (also Prism)
        # ---------------------------
        boat1 = Prism(dimensions=[0.6, 0.4, 0.3])
        boat2 = Prism(dimensions=[0.6, 0.4, 0.3])

        boat1.set_fill(ORANGE, opacity=1)
        boat2.set_fill(ORANGE, opacity=1)

        boat1.move_to(LEFT * 4 + UP * 2)
        boat2.move_to(RIGHT * 4 + DOWN * 2)

        self.play(Create(axle), FadeIn(wheel_group), FadeIn(boat1), FadeIn(boat2))
        self.wait(1)

        # =================================================
        # STEP 1 — Boats enter
        # =================================================
        self.play(
            boat1.animate.move_to(caisson_top.get_center()),
            boat2.animate.move_to(caisson_bottom.get_center()),
            run_time=3
        )
        self.wait(1)

        # =================================================
        # STEP 2 — Balanced
        # =================================================
        new_text = Text("2. System Balanced").scale(0.6)
        new_text.to_edge(UP)
        self.play(Transform(step_text, new_text))

        balance_line = Line(LEFT * 2, RIGHT * 2)
        balance_line.shift(DOWN * 3)
        balance_line.set_color(GREEN)

        self.play(Create(balance_line))
        self.wait(2)
        self.play(FadeOut(balance_line))

        # =================================================
        # STEP 3 — Rotate
        # =================================================
        new_text2 = Text("3. Wheel Rotates").scale(0.6)
        new_text2.to_edge(UP)
        self.play(Transform(step_text, new_text2))

        self.play(
            Rotate(wheel_group, angle=PI, about_point=ORIGIN),
            Rotate(boat1, angle=PI, about_point=ORIGIN),
            Rotate(boat2, angle=PI, about_point=ORIGIN),
            run_time=4
        )
        self.wait(1)

        # =================================================
        # STEP 4 — Exit
        # =================================================
        new_text3 = Text("4. Boats Exit").scale(0.6)
        new_text3.to_edge(UP)
        self.play(Transform(step_text, new_text3))

        self.play(
            boat1.animate.shift(RIGHT * 4),
            boat2.animate.shift(LEFT * 4),
            run_time=3
        )

        self.wait(2)
