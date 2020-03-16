SERVICE="observer_app"
PY_DIR="observer_app"

BC_PROTO_F = proto/blockchain_gateway.proto
TRX_PROTO_F = proto/transactions.proto
EXC_PROTO_F = proto/exchanger.proto
LOAN_PROTO_F = proto/loan.proto
GAS_PROTO_F= proto/gasstation.proto
CUR_PROTO_F= proto/currencies.proto
PROTO_PATH= proto/wallets.proto


PROTOC_INCLUDE = \
	-I=/usr/local/include \
	-I proto/ \
	-I${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
	-I${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway

PROTOC = python3 -m grpc.tools.protoc


.PHONY: proto
proto: OUT_DIR=$(PY_DIR)/rpc

proto: $(PROTO_PATH)
	mkdir -p $(OUT_DIR)
	$(PROTOC) $(PROTOC_INCLUDE) \
		--grpc_python_out=$(OUT_DIR) \
		--python_grpc_out=$(OUT_DIR) \
		--python_out=plugins=grpc:$(OUT_DIR) $(PROTO_PATH)
	sed -ie 's/protoc-gen-swagger/protoc_gen_swagger/g' $(OUT_DIR)/wallets_grpc.py

proto: bgw_proto transactions-proto loan-proto proto-gas cur_proto

bgw_proto: $(BC_PROTO_F)
	$(PROTOC) $(PROTOC_INCLUDE) \
		--grpc_python_out=$(OUT_DIR) \
		--python_grpc_out=$(OUT_DIR) \
		--python_out=plugins=grpc:$(OUT_DIR) $(BC_PROTO_F)
	sed -ie 's/protoc-gen-swagger/protoc_gen_swagger/g' $(OUT_DIR)/blockchain_gateway_grpc.py

transactions-proto: $(TRX_PROTO_F)
	$(PROTOC) $(PROTOC_INCLUDE) \
		--grpc_python_out=$(OUT_DIR) \
		--python_grpc_out=$(OUT_DIR) \
		--python_out=plugins=grpc:$(OUT_DIR) $(TRX_PROTO_F)
	sed -ie 's/protoc-gen-swagger/protoc_gen_swagger/g' $(OUT_DIR)/transactions_grpc.py

loan-proto: $(LOAN_PROTO_F)
	$(PROTOC) $(PROTOC_INCLUDE) \
		--grpc_python_out=$(OUT_DIR) \
		--python_grpc_out=$(OUT_DIR) \
		--python_out=plugins=grpc:$(OUT_DIR) $(LOAN_PROTO_F)
	sed -ie 's/protoc-gen-swagger/protoc_gen_swagger/g' $(OUT_DIR)/loan_grpc.py

proto-gas: $(GAS_PROTO_F)
	$(PROTOC) $(PROTOC_INCLUDE) \
		--grpc_python_out=$(OUT_DIR) \
		--python_grpc_out=$(OUT_DIR) \
		--python_out=plugins=grpc:$(OUT_DIR) $(GAS_PROTO_F)
	sed -ie 's/protoc-gen-swagger/protoc_gen_swagger/g' $(OUT_DIR)/gasstation_grpc.py

cur_proto: $(CUR_PROTO_F)
	$(PROTOC) $(PROTOC_INCLUDE) \
		--grpc_python_out=$(OUT_DIR) \
		--python_grpc_out=$(OUT_DIR) \
		--python_out=plugins=grpc:$(OUT_DIR) $(CUR_PROTO_F)
	sed -ie 's/protoc-gen-swagger/protoc_gen_swagger/g' $(OUT_DIR)/currencies_grpc.py
