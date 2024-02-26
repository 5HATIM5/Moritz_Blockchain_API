import datetime as _dt
import hashlib as _hl
import json as _json
from fastapi import File, UploadFile
from fastapi import HTTPException

"""
Blockchain Structure

Geneis Block
{
    index: 0,
    timestamp: current time,
    data: geneis block,
    proof: 32453,
    previous_hash: "0"
} -> hash() -> 234fgh
{
    index: 1,
    timestamp: current time,
    data: product data 1,
    proof: 2457364,
    previous_hash: 234fgh
} -> hash() -> 567ijk
{
    index: 2,
    timestamp: current time,
    data: product data 2,
    proof: 29465647,
    previous_hash: 567ijk
} -> hash() -> 891lmn

"""


class Blockchain:
    def __init__(self):
        self.chain = list()
        initial_block = self._create_block(
            product_hash="genesis block",
            # proof=1,
            previous_hash="0",
            index=1,
        )
        block_hash = _hl.sha256(str(initial_block).encode()).hexdigest()
        initial_block["block_hash"] = block_hash
        self.chain.append(initial_block)

    def mine_block(self, data: str) -> dict:
        previous_block = self.get_previous_block()
        # previous_proof = previous_block["proof"]
        index = len(self.chain) + 1
        # proof = self._proof_of_work(
        #     previous_proof=previous_proof,
        #     index=index,
        #     product_hash=product_hash,
        # )
        previous_hash = self._hash(block=previous_block)
        block = self._create_block(
            product_hash=data, previous_hash=previous_hash, index=index
        )
        # proof=proof
        block_hash = _hl.sha256(str(block).encode()).hexdigest()
        block["block_hash"] = block_hash
        self.chain.append(block)
        return block

    def _create_block(
        self, product_hash: str, previous_hash: str, index: int
    ) -> dict:
        # proof: int
        product_hash = _hl.sha256(str(product_hash).encode()).hexdigest()
        block = {
            "index": index,
            "timestamp": str(_dt.datetime.now()),
            "product_hash": product_hash,
            # "proof": proof,
            "previous_hash": previous_hash,
        }

        return block

    def get_previous_block(self) -> dict:
        return self.chain[-1]

    def _to_digest(
        self, new_proof: int, previous_proof: int, index: int, product_hash: str
    ) -> bytes:
        to_digest = str(new_proof**2 - previous_proof**2 + index) + product_hash
        # It returns an utf-8 encoded version of the string
        return to_digest.encode()

    def _proof_of_work(self, previous_proof: str, index: int, product_hash: str) -> int:
        new_proof = 1
        check_proof = False

        while not check_proof:
            to_digest = self._to_digest(new_proof, previous_proof, index, product_hash)
            hash_operation = _hl.sha256(to_digest).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def _hash(self, block: dict) -> str:
        """
        Hash a block and return the crytographic hash of the block
        """
        encoded_block = _json.dumps(block, sort_keys=True).encode()

        return _hl.sha256(encoded_block).hexdigest()

    def is_chain_valid(self) -> bool:
        previous_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            block = self.chain[block_index]
            # Check if the previous hash of the current block is the same as the hash of it's previous block
            if block["previous_hash"] != self._hash(previous_block):
                return False

            # previous_proof = previous_block["proof"]
            # index, product_hash = block["index"], block["product_hash"]
            # proof = block["proof"]
            # hash_operation = _hl.sha256(
            #     self._to_digest(
            #         # new_proof=proof,
            #         # previous_proof=previous_proof,
            #         index=index,
            #         product_hash=product_hash,
            #     )
            # ).hexdigest()

            # if hash_operation[:4] != "0000":
            #     return False

            previous_block = block
            block_index += 1

        return True

    def reset_chain(self):
        self.chain = list()
        initial_block = self._create_block(
            product_hash="genesis block",
            # proof=1,
            previous_hash="0",
            index=1,
        )
        block_hash = _hl.sha256(str(initial_block).encode()).hexdigest()
        initial_block["block_hash"] = block_hash
        self.chain.append(initial_block)

    def store_product_image(product_id: int, product_image: UploadFile = File(...)):
        try:
            filename = f"{product_id}_{(product_image.filename)}"
            with open(f"uploads/{filename}", "wb") as f:
                f.write(product_image.file.read())

            return {"Message": "Image uploaded successfully"}

        except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))