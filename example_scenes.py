#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

HEAD_INDEX = 0
BODY_INDEX = 1
ARMS_INDEX = 2
LEGS_INDEX = 3

SVG_IMAGE_DIR = "/home/fkobayashi/files/manim/media/designs/svg_images/"


class joinedKnot(SVGMobject):
    CONFIG = {
        "color": BLUE_E,
        "file_name_prefix": "7_2_joined",
        "stroke_width": 2,
        "stroke_color": WHITE,
        "fill_opacity": 0.0,
        "height": 5,
    }

    def __init__(self, mode="plain", knot_fname=None, **kwargs):
        digest_config(self, kwargs)
        if knot_fname is not None:
            self.file_name_prefix = knot_fname + "_joined"

        # print(knot_fname)

        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR, "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" % (self.file_name_prefix, mode))
            svg_file = os.path.join(SVG_IMAGE_DIR, "7_2_joined_plain.svg")
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)


class unjoinedKnot(SVGMobject):
    CONFIG = {
        "color": BLUE_E,
        "file_name_prefix": "7_2",
        "stroke_width": 2,
        "stroke_color": WHITE,
        "fill_opacity": 0.0,
        "height": 5,
    }

    def __init__(self, mode="plain", knot_fname=None, **kwargs):
        digest_config(self, kwargs)
        if knot_fname is not None:
            self.file_name_prefix = knot_fname

        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR, "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" % (self.file_name_prefix, mode))
            svg_file = os.path.join(SVG_IMAGE_DIR, "7_2_unjoined.svg")
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)


class Gaps(SVGMobject):
    CONFIG = {
        "color": BLUE_E,
        "file_name_prefix": "7_2_gaps",
        "stroke_width": 5,
        "stroke_color": BLACK,
        "fill_opacity": 0.0,
        "height": 4.175,
    }

    def __init__(self, mode="plain", **kwargs):
        digest_config(self, kwargs)
        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR, "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" % (self.file_name_prefix, mode))
            svg_file = os.path.join(SVG_IMAGE_DIR, "gaps_plain.svg")
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)


class Construct72(Scene):
    def construct(self):
        start_knot = joinedKnot()
        # end_knot = unjoinedKnot()
        mygaps = Gaps()
        mygaps.shift(0.083 * DOWN + 0.11 * RIGHT)

        circle = Circle(radius=2.5)

        self.play(ShowCreation(circle))
        self.play(Transform(circle, start_knot, run_time=5))
        self.play(FadeIn(mygaps, run_time=1))
        self.wait(2)


class Construct72Line(Scene):
    def construct(self):
        start_knot = joinedKnot()
        # end_knot = unjoinedKnot()
        mygaps = Gaps()
        mygaps.shift(0.083 * DOWN + 0.11 * RIGHT)

        # circle = Circle(radius=2.5)
        line = Line(np.array([-3, 0, 0]), np.array([3, 0, 0]))
        # line2 = Line(np.array([-5, 0, -1]), np.array([-2, 0, -1]), stroke_color=BLACK)

        self.play(ShowCreation(line))
        self.play(Transform(line, start_knot, run_time=4))
        self.play(FadeIn(mygaps, run_time=1))
        self.wait(2)


class Construct72CommDiag(Scene):
    def construct(self):
        #######################################################
        # Scale the stuff up top
        scalefac = 0.4

        # Define the top shift value
        tshift = 4 * LEFT + 2.5 * UP

        # Instantiate
        start_knot = joinedKnot(stroke_color=BLUE_C)
        start_knot_b = joinedKnot(stroke_color=YELLOW_D)
        tgaps = Gaps()
        bgaps = Gaps()
        tline = Line(np.array([-4, 0, 0]), np.array([2, 0, 0]))
        tlrcopy = Line(np.array([-4, 0, 0]), np.array([2, 0, 0]), stroke_color=BLUE_C)
        tlbcopy = Line(np.array([-4, 0, 0]), np.array([2, 0, 0]), stroke_color=RED_C)

        # Instantiate Lower stuff
        bcircle = Circle(radius=1)
        bcircle.shift(1.8 * DOWN)

        # # Add dots in
        # zdot = Dot()
        # zdot.shift(4 * LEFT)
        # odot = Dot()
        # odot.shift(2 * RIGHT)
        # tline.add(zdot)
        # tline.add(odot)

        # bcdot = Dot(color=RED_C)
        # bcdot2 = Dot(color=RED_C)
        # bcdot.shift(1.8 * DOWN, 1 * RIGHT)
        # bcdot2.shift(1.8 * DOWN, 1 * RIGHT)
        # bcircle.add(bcdot)
        # bcircle.add(bcdot2)

        # rdot = Dot()
        # rdot.shift(0.5 * DOWN + 0.5 * LEFT)

        # start_knot.add(rdot)
        # start_knot_b.add_to_back(rdot)

        # Arrows
        tarrow = Arrow(tshift + 1 * RIGHT, tshift + 7 * RIGHT, stroke_color=BLUE_C)
        blarrow = Arrow(
            tshift + 0.71 * RIGHT + 0.71 * DOWN,
            1.8 * DOWN + 0.71 * LEFT + 0.71 * UP,
            stroke_color=RED_C,
        )

        brarrow = Arrow(
            1.8 * DOWN + 0.71 * RIGHT + 1 * UP,
            tshift + 1 * DOWN + 1 * LEFT + 8 * RIGHT,
            stroke_color=YELLOW_C,
        )

        # Apply the appropriate scalings
        tgaps.shift((0.083 * DOWN + 0.11 * RIGHT) * scalefac)
        bgaps.shift((0.083 * DOWN + 0.11 * RIGHT) * scalefac)
        start_knot.scale(scalefac)
        start_knot_b.scale(scalefac)
        tgaps.scale(scalefac)
        bgaps.scale(scalefac)
        tline.scale(scalefac)
        tlrcopy.scale(scalefac)
        tlbcopy.scale(scalefac)

        # Apply the shifts
        start_knot.shift(tshift + 8 * RIGHT)
        start_knot_b.shift(tshift + 8 * RIGHT)
        tgaps.shift(tshift + 8 * RIGHT)
        bgaps.shift(tshift + 8 * RIGHT)
        tline.shift(tshift)
        tlrcopy.shift(tshift)
        tlbcopy.shift(tshift)

        tlabel = TextMobject(r"$K'_{(7,2)}$")
        tlabel.shift(3 * UP)
        tlabel.set_color(BLUE_C)

        bllabel = TextMobject(r"$\pi_{[0 \sim 1]}$")
        bllabel.shift(0.125 * DOWN + 3 * LEFT)
        bllabel.set_color(RED_C)

        brlabel = TextMobject(r"$K_{(7,2)}$")
        brlabel.shift(0.125 * DOWN + 2.5 * RIGHT)
        brlabel.set_color(YELLOW_D)

        for myobj in [bcircle, tline, tlrcopy, tlbcopy, start_knot, start_knot_b]:
            myobj.update()

        self.play(ShowCreation(tline))
        self.play(Transform(tlrcopy, start_knot, run_time=2.5))
        self.play(FadeIn(tgaps, run_time=0.5))
        self.play(Transform(tlbcopy, bcircle, run_time=2.5))
        self.play(Transform(bcircle, start_knot_b, run_time=2.5))
        self.play(FadeIn(bgaps, run_time=0.5))

        self.wait(1)

        self.play(
            *[
                ShowCreation(a)
                for a in [blarrow, brarrow, tarrow, tlabel, bllabel, brlabel]
            ]
        )

        self.wait(2)


class Construct31(Scene):
    def construct(self):
        start_knot = joinedKnot(knot_fname="3_1")
        # end_knot = unjoinedKnot()
        # mygaps = Gaps()
        # mygaps.shift(0.083 * DOWN + 0.11 * RIGHT)
        # waving_man = testKnot("wave")

        circle = Circle(radius=2.5)

        self.play(ShowCreation(circle))
        self.play(Transform(circle, start_knot, run_time=5))
        # self.play(FadeIn(mygaps))


class Construct41(Scene):
    def construct(self):
        start_knot = joinedKnot(knot_fname="4_1")
        # end_knot = unjoinedKnot()
        # mygaps = Gaps()
        # mygaps.shift(0.083 * DOWN + 0.11 * RIGHT)
        # waving_man = testKnot("wave")

        circle = Circle(radius=2.5)

        self.play(ShowCreation(circle))
        self.play(Transform(circle, start_knot, run_time=5))
        # self.play(FadeIn(mygaps))


class Construct51(Scene):
    def construct(self):
        start_knot = joinedKnot(knot_fname="5_1")

        circle = Circle(radius=2.5)

        self.play(ShowCreation(circle))
        self.play(Transform(circle, start_knot, run_time=5))


# Why not perform all the requisite Reidemeister moves _first_, then
# perform a sequence of crossing changes?


class Construct52(Scene):
    def construct(self):
        start_knot = joinedKnot(knot_fname="5_2")

        circle = Circle(radius=2.5)

        self.play(ShowCreation(circle))
        self.play(Transform(circle, start_knot, run_time=5))


class Construct61(Scene):
    def construct(self):
        start_knot = joinedKnot(knot_fname="6_1")

        circle = Circle(radius=2.5)

        self.play(ShowCreation(circle))
        self.play(Transform(circle, start_knot, run_time=5))


class Construct62(Scene):
    def construct(self):
        start_knot = joinedKnot(knot_fname="6_2")

        circle = Circle(radius=2.5)

        self.play(ShowCreation(circle))
        self.play(Transform(circle, start_knot, run_time=5))


class Construct63(Scene):
    def construct(self):
        start_knot = joinedKnot(knot_fname="6_2")

        circle = Circle(radius=2.5)

        self.play(ShowCreation(circle))
        self.play(Transform(circle, start_knot, run_time=5))


class ConstructAll(Scene):
    def construct(self):

        col_3 = RED_D
        col_4 = YELLOW_D
        col_5 = BLUE_D
        col_6 = GREEN_C
        col_7 = PINK

        default_height = 1.5

        k31 = joinedKnot(
            height=default_height,
            knot_fname="3_1",
            stroke_color=col_3,
            stroke_width=2.5,
        )
        k41 = joinedKnot(height=default_height, knot_fname="4_1", stroke_color=col_4)
        k51 = joinedKnot(height=default_height, knot_fname="5_1", stroke_color=col_5)
        k52 = joinedKnot(height=default_height, knot_fname="5_2", stroke_color=col_5)
        k61 = joinedKnot(height=default_height, knot_fname="6_1", stroke_color=col_6)
        k62 = joinedKnot(height=default_height, knot_fname="6_2", stroke_color=col_6)
        k63 = joinedKnot(height=default_height, knot_fname="6_3", stroke_color=col_6)
        k71 = joinedKnot(height=default_height, knot_fname="7_1", stroke_color=col_7)
        k72 = joinedKnot(height=default_height, knot_fname="7_2", stroke_color=col_7)
        k73 = joinedKnot(height=default_height, knot_fname="7_3", stroke_color=col_7)
        k74 = joinedKnot(height=default_height, knot_fname="7_4", stroke_color=col_7)
        k75 = joinedKnot(height=default_height, knot_fname="7_5", stroke_color=col_7)
        k76 = joinedKnot(height=default_height, knot_fname="7_6")

        default_radius = 0.7

        c31 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c41 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c51 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c52 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c61 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c62 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c63 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c71 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c72 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c73 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c74 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c75 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)
        c76 = Circle(radius=default_radius, stroke_color=WHITE, stroke_width=2)

        # DEFINE S^1

        l31_a = TextMobject("$S^1$")
        l41_a = TextMobject("$S^1$")
        l51_a = TextMobject("$S^1$")
        l52_a = TextMobject("$S^1$")
        l61_a = TextMobject("$S^1$")
        l62_a = TextMobject("$S^1$")
        l63_a = TextMobject("$S^1$")
        l71_a = TextMobject("$S^1$")
        l72_a = TextMobject("$S^1$")
        l73_a = TextMobject("$S^1$")
        l74_a = TextMobject("$S^1$")
        l75_a = TextMobject("$S^1$")
        l76_a = TextMobject("$S^1$")

        # DEFINE TEXT FOR KNOT MAPS

        l31_b = TextMobject("$K_{(3,1)}$")
        l41_b = TextMobject("$K_{(4,1)}$")
        l51_b = TextMobject("$K_{(5,1)}$")
        l52_b = TextMobject("$K_{(5,2)}$")
        l61_b = TextMobject("$K_{(6,1)}$")
        l62_b = TextMobject("$K_{(6,2)}$")
        l63_b = TextMobject("$K_{(6,3)}$")
        l71_b = TextMobject("$K_{(7,1)}$")
        l72_b = TextMobject("$K_{(7,2)}$")
        l73_b = TextMobject("$K_{(7,3)}$")
        l74_b = TextMobject("$K_{(7,4)}$")
        l75_b = TextMobject("$K_{(7,5)}$")
        l76_b = TextMobject("$K_{(7,6)}$")

        # SET COLORS OF THE KNOT MAPS

        l31_b.set_color(col_3)
        l41_b.set_color(col_4)

        l51_b.set_color(col_5)
        l52_b.set_color(col_5)

        l61_b.set_color(col_6)
        l62_b.set_color(col_6)
        l63_b.set_color(col_6)

        l71_b.set_color(col_7)
        l72_b.set_color(col_7)
        l73_b.set_color(col_7)
        l74_b.set_color(col_7)
        l75_b.set_color(col_7)
        l76_b.set_color(col_7)

        # scaling

        text_scale = 0.6

        l31_b.scale(text_scale)
        l41_b.scale(text_scale)
        l51_b.scale(text_scale)
        l52_b.scale(text_scale)
        l61_b.scale(text_scale)
        l62_b.scale(text_scale)
        l63_b.scale(text_scale)
        l71_b.scale(text_scale)
        l72_b.scale(text_scale)
        l73_b.scale(text_scale)
        l74_b.scale(text_scale)
        l75_b.scale(text_scale)
        l76_b.scale(text_scale)

        yspace = 2.75
        yshift = 0.25

        data = [
            (k31, c31, 4.5 * LEFT + (yspace + yshift) * UP, l31_a, l31_b),
            (k41, c41, 1.5 * LEFT + (yspace + yshift) * UP, l41_a, l41_b),
            (k51, c51, 1.5 * RIGHT + (yspace + yshift) * UP, l51_a, l51_b),
            (k52, c52, 4.5 * RIGHT + (yspace + yshift) * UP, l52_a, l52_b),
            (k61, c61, 4.5 * LEFT + yshift * UP, l61_a, l61_b),
            (k62, c62, 1.5 * LEFT + yshift * UP, l62_a, l62_b),
            (k63, c63, 1.5 * RIGHT + yshift * UP, l63_a, l63_b),
            (k71, c71, 4.5 * RIGHT + yshift * UP, l71_a, l71_b),
            (k72, c72, 4.5 * LEFT + (yspace - yshift) * DOWN, l72_a, l72_b),
            (k73, c73, 1.5 * LEFT + (yspace - yshift) * DOWN, l73_a, l73_b),
            (k74, c74, 1.5 * RIGHT + (yspace - yshift) * DOWN, l74_a, l74_b),
            (k75, c75, 4.5 * RIGHT + (yspace - yshift) * DOWN, l75_a, l75_b),
            (
                k76,
                c76,
                9.5 * RIGHT + yspace * DOWN,
                l76_a,
                l76_b,
            ),  # For some reason the
            # last element always gets messed up, so we'll just pass
            # an extra one for now
        ]

        for k, c, thisshift, atext, btext in data:
            k.shift(thisshift)
            c.shift(thisshift)
            atext.shift(thisshift + 1.1 * DOWN)
            btext.shift(thisshift + 1.1 * DOWN)

        toplay = [ShowCreation(c, run_time=2) for _, c, _, _, _ in data]  # + [

        self.play(*toplay)

        self.wait(2)

        totransform = [
            Transform(c, k, run_time=5, rate_func=smooth) for k, c, _, _, _ in data
        ]

        labels = [FadeIn(btext, run_time=2) for _, _, _, _, btext in data]

        self.play(*totransform)
        self.play(*labels)
        self.wait(2)
        # self.play(Transform(circle, start_knot, run_time=5))
        # self.play(FadeIn(mygaps))
