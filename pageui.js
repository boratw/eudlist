
let item_size = "";
let address_size = "";
let offsetname_size = "";



function ExpandItem(elem)
{
    unionname = elem.getAttribute("name").replace("u_", "i_");
    for([key, item] of cur_search_dict)
    {
        if(item.hasAttribute("name"))
            if(item.getAttribute("name") == unionname)
                item.setAttribute("unioncollapse", "false");
    }
}

function CollapseItem(elem)
{
    unionname = elem.getAttribute("name").replace("u_", "i_");
    for([key, item] of cur_search_dict)
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
        if(target.className == "item address" || target.className == "item address large")
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
        else if(target.className == "item varname" || target.className == "item name function" || target.className == "item name variable")
        {
            text= target.innerHTML.replace(/\s+/g, '');
            navigator.clipboard.writeText(text);
        }
        else if(target.className.endsWith("description"))
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
        for (i of search_dicts[name])
        {
            if (i[0].includes(s))
            {
                i[1].hidden = false;
                
            }
            else
            {
                i[1].hidden = true;
            }
        }
    }
    else
    {
        for (i of search_dicts[name])
        {
            i[1].hidden = false;
        }
    }
}
