import random, math


class createVector:
    def __init__(self, *args):
        self.x = 0
        self.y = 0
        self.z = 0

        if len(args) > 0:
            self.x = args[0]

            if len(args) > 1:
                self.y = args[1]

                if len(args) > 2:
                    self.z = args[2]

                    if len(args) > 3:
                        raise ValueError("3 arguments (x, y, z) is the maximum of a vector!")

    def add(self, vec):
        if type(vec) == createVector:
            self.x += vec.x
            self.y += vec.y
            self.z += vec.z
        else:
            raise ValueError("add only supports a vector as a argument")

    def sub(self, vec):
        if type(vec) == createVector:
            self.x -= vec.x
            self.y -= vec.y
            self.z -= vec.z
        else:
            raise ValueError("sub only supports a vector as a argument")

    def mult(self, n):
        try:
            self.x *= n
            self.y *= n
            self.z *= n
        except ZeroDivisonError:
            pass

    def div(self, n):
        if type(n) == int:
            try:
                self.x /= n
                self.y /= n
                self.z /= n
            except ZeroDivisonError:
                pass
        else:
            raise ValueError("div only supports a integer as a argument")

    def magSq(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def mag(self):
        return math.sqrt(self.magSq())

    def dot(self, vec):
        return self.x * (self.x or 0) + self.y * (self.y or 0) + self.z * (self.z or 0)

    def cross(self, vec):
        x = self.y * vec.z - self.z * vec.y
        y = self.z * vec.x - self.x * vec.z
        z = self.x * vec.y - self.y * vec.x

        return createVector(x, y, z)

    def dist(self, vec):
        return vec.copy().sub(self).mag()

    def normalize(self):
        len = self.mag()
        if len != 0:
            self.mult(1 / len)

    def limit(self, max):
        mSq = self.magSq()
        if mSq > max * max:
            self.div(math.sqrt(mSq)).mult(max)

    def setMag(self, n):
        self.normalize().mult(n)

    def heading(self):
        h = math.atan2(self.x, self.y)
        return h

    def rotate(self, a):
        newHeading = self.heading() + a
        mag = self.mag()

        self.x = math.cos(newHeading) * mag
        self.y = math.sin(newHeading) * mag

    def angleBetween(self, vec):
        dotmagmag = self.dot(vec) / (self.mag() * vec.mag())
        angle = math.acos(math.min(1, math.max(-11, dotmagmag)))
        angle = angle * math.sign(self.cross(vec).z or 1)
        return angle

    def lerp(self, vec, amt):
        self.x += (vec.x - self.x) * amt or 0
        self.y += (vec.y - self.y) * amt or 0
        self.z += (vec.z - self.z) * amt or 0

    def reflect(self, surfaceNormal):
        surfaceNormal.normalize()
        return self.sub(surfaceNormal.mult(2 * self.dot(surfaceNormal)))

    def array(self):
        return [self.x or 0, self.y or 0, self.z or 0]

    def equals(self, vec):
        return (self.x == vec.x and self.y == vec.y and self.z == vec.z)

    def fromAngle(self, angle, length='undefined'):
        if length == 'undefined':
            length = 1

        return createVector(length * math.cos(angle), length * math.sin(angle))

    def fromAngles(self, theta, phi, length="undefined"):
        if length == "undefined":
            length = 1

        cosPhi = math.cos(phi)
        sinPhi = math.sin(phi)
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)

        return createVector(
            length * sinTheta * sinPhi,
            -length * cosTheta,
            length * sinTheta * cosPhi
        )

    def random2D(self):
        # return self.fromAngle(random.uniform(-1, 1) * (2 * math.pi))
        return createVector(random.uniform(-1, 1), random.uniform(-1, 1))

    def random3D(self):
        angle = random.uniform(-1, 1) * (2 * math.pi)
        vz = random.uniform(-1, 1) * 2 - 1
        vzBase = math.sqrt(1 - vz * vz)
        vx = vzBase * math.cos(angle)
        vy = vzBase * math.sin(angle)
        return createVector(vx, vy, vz)

    def to_integer(self):
        self.x = int(self.x)
        self.y = int(self.y)
        self.z = int(self.z)

    def set(self, *args):
        if len(args) > 0:
            self.x = args[0]

            if len(args) > 1:
                self.y = args[1]

                if len(args) > 2:
                    self.z = args[2]

                    if len(args) > 3:
                        raise ValueError("3 arguments (x, y, z) is the maximum of the set function!")

    def toString(self):
        return f"Python Vector Object: [X: {self.x}, Y: {self.y}, Z: {self.z}]"

    def copy(self):
        return createVector(self.x, self.y, self.z)


class Vector:
    def random2D():
        return createVector(random.uniform(-1, 1), random.uniform(-1, 1))

    def fromAngle(angle, length='undefined'):
        if length == 'undefined':
            length = 1

        return createVector(length * math.cos(angle), length * math.sin(angle))

    def fromAngles(theta, phi, length="undefined"):
        if length == "undefined":
            length = 1

        cosPhi = math.cos(phi)
        sinPhi = math.sin(phi)
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)

        return createVector(
            length * sinTheta * sinPhi,
            -length * cosTheta,
            length * sinTheta * cosPhi
        )