module hbm_policy_controller(
  input [7:0] bandwidth_pressure,
  input [7:0] thermal_pressure,
  input [7:0] qtime_risk,
  input [7:0] margin_risk,
  output reg [2:0] selected_policy,
  output reg requires_supervisor_gate
);
always @* begin
  requires_supervisor_gate = (margin_risk > 8'd160) || (qtime_risk > 8'd180);
  if (thermal_pressure > 8'd170) selected_policy = 3'd3;
  else if (margin_risk > 8'd140) selected_policy = 3'd5;
  else if (bandwidth_pressure > 8'd150) selected_policy = 3'd1;
  else selected_policy = 3'd0;
end
endmodule
