
let item_size = "";
let address_size = "";
let offsetname_size = "";

let searchdict = {}


function ExpandItem(elem)
{
    unionname = elem.getAttribute("name").replace("u_", "i_");
    for([key, item] of searchdict)
    {
        if(item.hasAttribute("name"))
            if(item.getAttribute("name") == unionname)
                item.setAttribute("unioncollapse", "false");
    }
}

function CollapseItem(elem)
{
    unionname = elem.getAttribute("name").replace("u_", "i_");
    for([key, item] of searchdict)
    {
        if(item.hasAttribute("name"))
            if(item.getAttribute("name") == unionname)
                item.setAttribute("unioncollapse", "true");
    }
}

function OnClickItem(e)
{
    target = e.target;
    if(target)
    {
        if(target.className == "item address")
        {
            text= target.innerHTML.replace(/\s+/g, '');
            if(text.length <= 5)
            {
                if(text[2] == "0")
                {
                    if((text[3]) == "0")
                        text = "0x" + text[4]
                    else
                        text = "0x" + text[3] + text[4]
                }
            }
            navigator.clipboard.writeText(text);
        }
        else if(target.className == "item varname")
        {
            text= target.innerHTML.replace(/\s+/g, '');
            navigator.clipboard.writeText(text);
        }
        else if(target.getAttribute("name") == "description")
        {
            return;
        }
        else
        {
            while(!target.className.startsWith("itembox"))
            {
                target = target.parentElement;
                if(!target)
                    return;
            }
            opened = target.getAttribute("active");
            if (opened == "true")
                opened = false
            else
                opened = true
            target.setAttribute("active", opened);
            if(target.className == "itembox uniongroup")
            {
                if(opened)
                    ExpandItem(target);
                else
                    CollapseItem(target);
            }
            else
            {
                for(node of target.children)
                {
                    if(node.className == "descbox")
                        node.hidden = !opened;
                }

            }
    
        }

    }
}


function TextInput(name)
{
    
    if (document.getElementById(name + "_search").value.length > 0)
    {
        let s = document.getElementById(name + "_search").value.toLowerCase();
        for (i of searchdict[name])
        {
            if (i[0].includes(s))
            {
                i[1].hidden = false;
                if(i[1].getAttribute("unioncollapse") == "true")
                {
                    ExpandItem(document.getElementsByName(i[1].getAttribute("name").replace("i_", "u_"))[0])
                }
            }
            else
            {
                i[1].hidden = true;
            }
        }
    }
    else
    {
        for (i of searchdict[name])
        {
            i[1].hidden = false;
        }
    }
}
