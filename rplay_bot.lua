do 

local function run(msg, matches) 

if ( msg.text ) then

  if ( msg.to.type == "user" ) then

     return  "للتحدث مع المطور اضغط على المعرف التالي \n @O_q1j \n  👾 "
     
  end 
   
end 

-- #DEV @O_q1j

end 

return { 
  patterns = { 
       "(.*)$"
  }, 
  run = run, 
} 

end 
-- By @O_q1j
