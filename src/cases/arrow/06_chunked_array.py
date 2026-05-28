import pyarrow as pa

# ChunkedArray = zero-copy list of contiguous arrays
chunks  = [pa.array([1, 2, 3]), pa.array([4, 5])]
chunked = pa.chunked_array(chunks)

print(chunked)
print("num_chunks:", chunked.num_chunks)
print("total len:", len(chunked))
