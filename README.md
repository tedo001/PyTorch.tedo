
Layer	What it does	Used in
nn.Linear(in, out)	Fully connected: y = Wx + b	Classifiers, heads
nn.Conv2d(in_ch, out_ch, kernel)	Detect spatial patterns in images	YOLO, CNNs
nn.ReLU()	max(0, x) — adds non-linearity	Every deep network
nn.BatchNorm2d(ch)	Normalises activations, stabilises training	YOLO uses this heavily
nn.Dropout(p)	Randomly zeros outputs — prevents overfitting	Classifiers
nn.Sigmoid()	Squashes output to 0–1 (probability)	Binary classification
nn.Softmax(dim)	Converts logits to probabilities summing to 1	Multi-class outputs
