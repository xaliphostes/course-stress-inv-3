from Data import Data
import RemoteStress
from tools import dot
import math


class Joint(Data):
    def cost(self, r: RemoteStress) -> float:
        return 1.0 - math.fabs(dot(self.n, r.S3))
