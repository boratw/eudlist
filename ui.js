
let prev_page = null;
let loaded_pages = {};

function OnNavBtn1Clicked(p)
{
    elem = document.getElementById(p);
    elem.setAttribute("active", "false")
    for(node of elem.children)
    {
        if(node.className == "navbtn child")
        {
            node.hidden = !node.hidden

        }
    }
}

function OpenPage(name)
{
    if(prev_page)
    {
        prev_page.setAttribute("active", "false");
    }
    
    if(!(name in loaded_pages))
        LoadPage(name);

    loaded_pages[name].setAttribute("active", "true");
    prev_page = loaded_pages[name]
}
function LoadPage(name)
{
    elem = document.createElement("div");
    elem.className = "page"
    document.getElementById("main").appendChild(elem);
    loaded_pages[name] = elem;
    LoadStart(name);
    
}

function OnLoad()
{
    loaded_pages["Credit"] = document.getElementById("credit");
    OnResize();
}
function OnResize()
{
    emsize = parseFloat(getComputedStyle(document.body).fontSize);
    if(document.body.clientWidth > emsize * 70)
        document.getElementById("actualbody").style.width = "70em";
    else
        document.getElementById("actualbody").style.width = "100%";


    if(document.getElementById("actualbody").clientWidth < emsize * 50)
        document.getElementById("main").style.width = "50em";
    else
        document.getElementById("main").style.width = "100%";
}

