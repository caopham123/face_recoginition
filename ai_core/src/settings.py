from insightface.app import FaceAnalysis
import insightface

MODEL_PATH = "buffalo_l"
MODEL_LOAD = FaceAnalysis(name=MODEL_PATH, allowed_modules="detection", providers=['CPUExecutionProvider'])
MODEL_LOAD.prepare(ctx_id=0, det_size=(640,640))