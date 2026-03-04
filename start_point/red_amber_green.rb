
lambda { |stdout,stderr,status|
  output = stdout + stderr
  return :red   if /FAILED \(failures=/.match(output)
  return :green if /OK/.match(output)
  return :amber
}
