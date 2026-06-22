module hbm_policy_proxy(input logic clk, input logic valid, output logic ready); always_ff @(posedge clk) ready <= valid; endmodule
