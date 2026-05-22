do 

local function run(msg, matches) 

if ( msg.text ) then

  if ( msg.to.type == "user" ) then

     return  "للتحدث مع المطور اضغط على المعرف التالي \n https://karboai.com/user/ims2t \n  👾 "
     
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
